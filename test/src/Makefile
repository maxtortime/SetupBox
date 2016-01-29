CC = gcc
OBJS = SetupBox_test.o
TARGET = SetupBox_test

all : $(TARGET)
$(TARGET):$(OBJS)
	$(CC) -o $@ $(OBJS) -lcunit

clean :
	rm -f $(OBJS) $(TARGET)
