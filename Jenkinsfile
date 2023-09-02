pipeline {
  agent any
  
  environment {
    BUILD_VERSION = "${BUILD_NUMBER}"
    DOCKER_REGISTRY = "alishazaei"
    DOCKER_REPO = "zoomedia"
    DOCKER_IMAGE_TAG = "${DOCKER_REGISTRY}/${DOCKER_REPO}:${APP_VERSION}"
  }

  stages {

  stage('Installing Bump') {
      steps {
        script {
          sh 'docker build  -f docker/production.Dockerfile -t test .'
          def APP_VERSION = sh 'docker run --rm test bump --patch'
        }
      }
    }

    stage('Set version') {
      steps {
        script {
          def VERSION
          script {
           VERSION = "${env.APP_VERSION}-${BUILD_VERSION}"
          }
          sh "echo VERSION Number :  ${VERSION} "
        }
      }
    }

    stage('Docker login to Docker Hub') {
      steps {
        script {
          withCredentials([usernamePassword(credentialsId: '6140a374-aa4e-4fa0-9187-aef779023cc8	', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
            sh "docker login -u $USERNAME -p $PASSWORD"
          }
        }
      }
    }

    stage('Build and push Docker image') {
      steps {
        script {
            sh "docker build -t ${DOCKER_REGISTRY}/${DOCKER_REPO}:v${VERSION} -f docker/production.Dockerfile ."
            sh "docker push ${DOCKER_REGISTRY}/${DOCKER_REPO}:v${VERSION}"

        }
      }
    }








  }
}
