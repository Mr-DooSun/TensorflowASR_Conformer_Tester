# TensorflowASR_Conformer_Tester

##### https://github.com/TensorSpeech/TensorFlowASR 해당 링크의 코드를 활용하였습니다.

#### < Conda env Setting >
<pre>
conda create -n test python==3.8.8
conda activate test
pip install tensorflow-gpu
pip install pyyaml
pip install tqdm
pip install librosa
pip install tensorflow-io --user
pip install sentencepiece
pip install tensorflow_datasets
pip install streamlit
</pre>

#### < Run >
<pre>
streamlit run STT_System.py
</pre>

#### < Result >
![](result.jpg)