FROM docker:18.02.0-ce-git
ENV CLOUD_SDK_VERSION 191.0.0

ENV PATH /google-cloud-sdk/bin:$PATH

RUN apk --no-cache add \
      curl \
      python2 \
      py-crcmod \
      bash \
      libc6-compat \
      openssh-client \
      git

RUN curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz \
 && tar xzf google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz \
 && rm google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz \
 && ln -s /lib /lib64 \
 && gcloud config set core/disable_usage_reporting true \
 && gcloud config set component_manager/disable_update_check true \
 && gcloud config set metrics/environment github_docker_image \
 && gcloud --version

RUN cd /usr/local/bin \
 && curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.9.3/bin/linux/amd64/kubectl \
 && chmod +x /usr/local/bin/kubectl
