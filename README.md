# TensorflowASR_Conformer_Tester

##### https://github.com/TensorSpeech/TensorFlowASR 해당 링크의 코드를 활용하였습니다.

###### [ Way ]
<pre>
<code>
conda create -n test python==3.8
conda activate test
conda install tensorflow-gpu
pip3 install '.[tf-2.5-gpu]'
</code>
</pre>

###### [ Check if the gpu is in use ]
<code>
python
tf.test.is_gpu_available()
exit()
</code>

###### [ if the gpu is not in use ]
<pre>
<code>
conda uninstall tensorflow-gpu
conda install tensorflow-gpu
</code>
</pre>

###### [ if the gpu is in use ]
<pre>
<code>
pip uninstall tensorflow-io
pip install tensorflow-io==0.15.0
pip uninstall librosa
conda install -c conda-forge librosa==0.7.2
pip uninstall numba
conda install numba==0.48.0
</code>
</pre>