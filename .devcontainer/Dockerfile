FROM musicscience37/sphinx-doxygen

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    openssh-client \
    gnupg2 \
    vim \
    nano \
    sudo \
    && \
    apt-get autoremove && \
    apt-get autoclean && \
    rm -r /var/lib/apt/lists/* && \
    # Make ubuntu user able to use sudo command.
    echo ubuntu ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/ubuntu && \
    chmod 0440 /etc/sudoers.d/ubuntu && \
    # Allow use of pyenv from ubuntu user.
    chmod 0777 /root && \
    chmod -R 0777 /root/.pyenv

# Prepare poetry for ubuntu user.
USER ubuntu
WORKDIR /home/ubuntu
ENV PATH="/home/ubuntu/.local/bin:$PATH"
RUN pipx install poetry
