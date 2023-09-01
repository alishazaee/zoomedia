pipeline {
  agent any
  
  environment {
    APP_VERSION = "${BUILD_NUMBER}"
    DOCKER_REGISTRY = "alishazaee"
    DOCKER_REPO = "zoomedia"
    DOCKER_IMAGE_TAG = "${DOCKER_REGISTRY}/${DOCKER_REPO}:${APP_VERSION}"
  }

  stages {

    stage('Set version') {
      steps {
        script {
          sh "echo VERSION Number :  ${env.APP_VERSION} "
        }
      }
    }

    stage('Build and push Docker image') {
      steps {
        script {
          def dockerImage = docker.build(env.DOCKER_IMAGE_TAG, '-f docker/production.Dockerfile .')
        }
      }
    }


  }
}
