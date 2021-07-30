# TensorflowASR_Conformer_Tester

##### https://github.com/TensorSpeech/TensorFlowASR 해당 링크의 코드를 활용하였습니다.

###### [ Way ]
<pre>
conda create -n test python==3.8
conda activate test
conda install tensorflow-gpu
pip3 install '.[tf-2.5-gpu]'
</pre>

###### [ Check if the gpu is in use ]
<pre>
python
tf.test.is_gpu_available()
exit()
</pre>

###### [ if the gpu is not in use ]
<pre>
conda uninstall tensorflow-gpu
conda install tensorflow-gpu
</pre>

###### [ if the gpu is in use ]
<pre>
pip uninstall tensorflow-io
pip install tensorflow-io==0.15.0
pip uninstall librosa
conda install -c conda-forge librosa==0.7.2
pip uninstall numba
conda install numba==0.48.0
</pre>