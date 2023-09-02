pipeline {
  agent any
  
  environment {
    BUILD_VERSION = "${BUILD_NUMBER}"
    DOCKER_REGISTRY = "alishazaei"
    DOCKER_REPO = "zoomedia"
    DOCKER_IMAGE_TAG = "${DOCKER_REGISTRY}/${DOCKER_REPO}:${APP_VERSION}"
  }

  stages {

  stage('Bumping Version') {

      steps {
        script {
          sh 'docker build  -f docker/production.Dockerfile -t test .'
          sh 'docker run test bash'
         
          def OUTPUT = sh(script:'docker exec test bump --patch',returnStdout: true).trim()
          env.APP_VERSION = OUTPUT
          sh 'echo ${APP_VERSION}'
          withCredentials([usernamePassword(credentialsId: 'ff8ef423-6aad-4705-a6f1-a06756855de3', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
            sh 'docker exec test git config --global user.email "jenkins@example.com"'
            sh 'docker exec test git config --global user.name jenkins'


            sh "docker exec test git remote origin https://$USERNAME:$PASSWORD@github.com/alishb80/zoomedia.git"
            sh 'docker exec test git add .'
            sh 'docker exec test git commit -m "ci-pipeline version bumping"'
            sh 'docker exec test git push origin HEAD:master'

          }

        }
      }
    }

    stage('Set version') {
      steps {
        script {

           def VERSION = "${env.APP_VERSION}-${BUILD_VERSION}"
           env.VERSION = VERSION

          sh "echo VERSION Number :  ${env.VERSION} "
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
