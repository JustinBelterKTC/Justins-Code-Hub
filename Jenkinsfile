pipeline {

  agent any
  
  parameters {
    choice(name: 'branch',
           choices: 'fix-123\nmain',
           description: 'Which branch would you like to select?')
    string(name: 'filename',
           defaultValue: 'README.md',
           description: 'Enter the name of the file you would like to cat.')
  }

  options {

    buildDiscarder logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '5', daysToKeepStr: '', numToKeepStr: '5')

  }

  stages {
    
    stage('cat file') {

      when {

        branch "${params.branch}"

      }

      steps {

        sh '''

          cat ${params.filename}

        '''

      }

    }

  }

}
