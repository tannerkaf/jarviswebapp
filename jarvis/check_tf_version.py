import tensorflow as tf

if hasattr(tf, "version"):
    print("TensorFlow version:", tf.version.VERSION)
else:
    print("TensorFlow version not found.")
