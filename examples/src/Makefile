CC=gcc
SRCS= SetupBox_demo.c vcscontroller.c
OBJS = SetupBox_demo.o vcscontroller.o
TARGET = SetupBox_demo
LIB_NAME = libsetupbox.a
LIB = -lgit2

all : $(OBJS)
	ar -cvq $(LIB_NAME) $(OBJS)

$(TARGET) : $(OBJS)
	$(CC) -c  $(SRCS)

clean:
	rm -f $(OBJS) $(TARGET)
