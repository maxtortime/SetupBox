/*
 * SetupBox_demo.c
 * For testing SetupBox.
 * 
 * Author:	Jungmo Ahn <ajm100@ajou.ac.kr>
 *
 */

#include <stdio.h>
#include "vcscontroller.h"
#include <string.h>
#include <pthread.h>
#include <stdlib.h>
#include <unistd.h>

#define THREAD

//XXX: Need to talk about a length of username
char username[32];

#ifndef THREAD

int thread_id;
pthread_t thread;

/*
 * Initialize a thread for running sb_update()
 * @author: Jungmo Ahn
 * @return: return 0 on success, non-zero otherwise.
 * @todo: to specify what parameter is needed for sb_update
 *        now, it sets NULL(fourth parameter).
 */
enum _error_code_t do_sb_update()
{
	// enum _error_code_t ret;
	thread_id = pthread_create(&thread, NULL, sb_update, NULL);
}

#endif //THREAD

/*
 * Do sb_init()
 * @author: Jungmo Ahn
 * @return: return 0 on success, non-zero otherwise.
 * @todo: to specify what to do when an error occurs.
 */
enum _error_code_t do_sb_init(enum VCS vcs, const char* dir)
{
	enum _error_code_t ret = SB_ERR_NONE;
	int check_json = 0;
	ret  = sb_init(vcs, dir);

	getlogin_r(username, 32);
	// if there is an error,
	if(ret != SB_ERR_NONE) {
		//Do something for handilng an error
	}
	// if there is no json file,
	if(ret != SB_ERR_NOJSON) {
		//Do something for json
	}

	return ret;
}

int main(int argc, char** argv)
{
	int vcs = 1;
	char dir[BUFSIZ];
	enum _error_code_t ret = SB_ERR_NONE;

	sprintf(dir, "/Users/%s/.SetupBox",username);
	
	ret = do_sb_init(vcs, dir);
	
	// if there is an error, terminate SetupBox
	if(ret != SB_ERR_NONE) {
		printf("error occurs at sb_init()");
		exit(15);
	}
	
	return 0;

}
