#!/usr/bin/expect 

spawn scp RESULTS/Ph_Results.txt  wcjos@192.168.1.74:/Users/wcjos/Aquatic-Pi/CAMmod
#######################

expect {
-re ".*es.*o.*" {
    exp_send "yes\r"
    exp_continue
  }
  -re ".*sword.*" {
    exp_send "joseparis1;\r"
  }
}
interact

spawn scp RESULTS/Oxygen_Results.txt  wcjos@192.168.1.74:/Users/wcjos/Aquatic-Pi/CAMmod
#######################

expect {
-re ".*es.*o.*" {
    exp_send "yes\r"
    exp_continue
  }
  -re ".*sword.*" {
    exp_send "joseparis1;\r"
  }
}
interact

spawn scp RESULTS/Temp_Results.txt  wcjos@192.168.1.74:/Users/wcjos/Aquatic-Pi/CAMmod
#######################

expect {
-re ".*es.*o.*" {
    exp_send "yes\r"
    exp_continue
  }
  -re ".*sword.*" {
    exp_send "joseparis1;\r"
  }
}
interact
