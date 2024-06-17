py_version=$1
tf_version=$2

podman build . --build-arg py_version=${py_version} --build-arg tf_version=${tf_version} --tag test_tf
podman run -it --rm test_tf
