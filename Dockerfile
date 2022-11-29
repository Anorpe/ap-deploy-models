FROM python:3.7.3-stretch

# Maintainer info
LABEL maintainer="aorregop@unal.edu.co"

# Make working directories
RUN  mkdir -p  /ap_deploy_models
WORKDIR  /ap_deploy_models

# Upgrade pip with no cache
RUN pip install --no-cache-dir -U pip

# Copy application requirements file to the created working directory
COPY requirements.txt .

# Install application dependencies from the requirements file
RUN pip install -r requirements.txt

# Copy every file in the source folder to the created working directory
COPY  . .

# Run the python application
CMD ["python", "main.py"]
