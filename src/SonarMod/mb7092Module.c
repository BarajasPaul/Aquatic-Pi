#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <termios.h>

//Copyright (C) 2015 Barajas D. Paul <Paul.Barajas@linux.com>

int main(int argc, char *argv[]){
    struct termios options;
    char Rx_port[]="/dev/ttyAMA0";

    //Open the serial port
    int fd_device = open(Rx_port, O_RDONLY);

    if (fd_device == -1){
        printf("Unable to read device");
        return 1;
    }

    //Configure serial port
    tcgetattr(fd_device, &options);
    options.c_cflag = B9600 | CS8 | CLOCAL | CREAD;
    options.c_iflag = IGNPAR;
    options.c_oflag = 0;
    options.c_lflag = 0;
    tcflush(fd_device, TCIFLUSH);
    tcsetattr(fd_device, TCSANOW, &options);

    if (fd_device != -1){
        unsigned char Rx_buffer[256];
        int Rx_length = read(fd_device, (void *)Rx_buffer, 255);
        if (Rx_length < 0){
            printf("No data");
        }else{
            Rx_buffer[Rx_length] = '\0';
            printf("%s\n", Rx_buffer);
        }
    }
    close(fd_device);
}
