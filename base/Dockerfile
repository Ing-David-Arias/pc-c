FROM jenkins/jenkins:lts

USER root

RUN apt-get update && \
    apt-get install -y wget gnupg2 && \
    wget https://github.com/adoptium/temurin21-binaries/releases/download/jdk-21.0.2%2B13/OpenJDK21U-jdk_x64_linux_hotspot_21.0.2_13.tar.gz -O openjdk-21.tar.gz && \
    mkdir -p /opt/java && \
    tar -xzf openjdk-21.tar.gz -C /opt/java && \
    rm openjdk-21.tar.gz && \
    update-alternatives --install /usr/bin/java java /opt/java/jdk-21.0.2+13/bin/java 1 && \
    update-alternatives --install /usr/bin/javac javac /opt/java/jdk-21.0.2+13/bin/javac 1 && \
    update-alternatives --set java /opt/java/jdk-21.0.2+13/bin/java && \
    update-alternatives --set javac /opt/java/jdk-21.0.2+13/bin/javac

USER jenkins
