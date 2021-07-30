# -*- coding: utf-8 -*-
from tensorflow_asr.utils import env_util
logger = env_util.setup_environment()

import tensorflow as tf
tf.keras.backend.clear_session()

mxp = False # Enable mixed precision
tf.config.optimizer.set_experimental_options({"auto_mixed_precision": mxp})

GPU_Device = [0] # Device's id to run test on
CPU = False # Whether to only use cpu
env_util.setup_devices(GPU_Device, cpu=CPU)

class STT() :
    config_file = 'config.yml' # The file path of model configuration file
    save_model = 'latest.h5' # Path to saved model
    assert save_model
    sentence_piece = False # Whether to use `SentencePiece` model
    subwords = True # Use subwords
    batch_size = 1 # Test batch size

    def __init__(self) :
        from tensorflow_asr_1.configs.config import Config
        from tensorflow_asr_1.datasets.asr_dataset import ASRSliceDataset
        from tensorflow_asr_1.featurizers.speech_featurizers import TFSpeechFeaturizer
        from tensorflow_asr_1.featurizers.text_featurizers import SubwordFeaturizer, SentencePieceFeaturizer, CharFeaturizer
        from tensorflow_asr_1.models.transducer.conformer import Conformer

        self.ASRSliceDataset = ASRSliceDataset
        self.Conformer = Conformer

        self.config = Config(self.config_file)
        self.speech_featurizer = TFSpeechFeaturizer(self.config.speech_config)

        if self.sentence_piece:
            logger.info("Use SentencePiece ...")
            self.text_featurizer = SentencePieceFeaturizer(self.config.decoder_config)
        elif self.subwords:
            logger.info("Use subwords ...")
            self.text_featurizer = SubwordFeaturizer(self.config.decoder_config)
        else:
            logger.info("Use characters ...")
            self.text_featurizer = CharFeaturizer(self.config.decoder_config)

        tf.random.set_seed(0)

        self.Model()

    def Model(self):
        # build model
        self.conformer = self.Conformer(**self.config.model_config, vocabulary_size=self.text_featurizer.num_classes)
        self.conformer.make(self.speech_featurizer.shape)
        self.conformer.load_weights(self.save_model, by_name=True)
        self.conformer.summary(line_length=100)
        self.conformer.add_featurizers(self.speech_featurizer, self.text_featurizer)

    def Test(self,data_path):
        self.test_dataset = self.ASRSliceDataset(
            speech_featurizer=self.speech_featurizer,
            text_featurizer=self.text_featurizer,
            **vars(self.config.learning_config.test_dataset_config)
        )

        self.test_data_loader = self.test_dataset.create(self.batch_size,data_path)

        results = self.conformer.predict(self.test_data_loader, verbose=1)

        for _,pred in enumerate(results) : 
            _, greedy, _ = [x.decode('utf-8') for x in pred]
            return greedy

# stt = STT()

# result = stt.Test('data/3240-131231-0000.flac')
# print(result)