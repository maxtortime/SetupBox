/*
 * SetupBox_demo.c
 * SetupBox demo app.
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

#define THREAD_UPDATE	 0
#define THREAD_COMMIT	 1
#define THREAD_TOTAL	 2

char		dir[256];
int		thread_id[THREAD_TOTAL];
pthread_t	thread[THREAD_TOTAL];
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;

/*
 * Initiailize SetupBox - Set dir path and signal
 * @author: Jungmo Ahn
 * @return: return 0 on success, non-zero otherwise.
 * @todo:
 */
int init()
{
	int ret;

	//if SetupBox is killed by user, call do_sb_destroy
	signal(SIGTERM, do_sb_destroy);
	ret = sprintf(dir, "%s/.SetupBox",getenv("HOME"));

	if ( ret <= 0 ) {
		return -1; 
	}
	else {
		return 0;
	}
}

/*
 * Create threads.
 * @author: Jungmo Ahn
 * @return: return 0 on success, non-zero otherwise.
 * @todo: Specifying what parameters are needed for sb_update
 * 	  now, these set NULL(fourth parameter).
 */
int create_threads()
{
	int i = 0;
	int ret = 0;
	thread_id[THREAD_COMMIT] = pthread_create(&thread_id[THREAD_COMMIT], NULL, sb_commit, NULL);
	thread_id[THREAD_UPDATE] = pthread_create(&thread_id[THREAD_UPDATE], NULL, sb_update, NULL);
	
	for(i = 0; i < THREAD_TOTAL; i++) {
		if(thread_id[i] == 0) {
			return -1;
		}
	}

	return 0;
}

/*
 * Printing error
 * @author: Jungmo Ahn
 * @todo: Specify and print error message, respectively.
 */
void printerror(enum _error_code_t ret)
{
	// if there is an error, terminate SetupBox
	printf("error occurs. error code : %d\n", ret);
	exit(15);
}

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

/*
 * Do sb_destory()
 * @author: Jungmo Ahn
 */
enum _error_code_t do_sb_destroy()
{
	enum _error_code_t ret = SB_ERR_NONE;

	//release mutex
	pthread_mutex_destroy(&mutex);

	ret = sb_destroy();
	
	if(ret != SB_ERR_NONE) {
		printerror(ret);
	}
	
	exit(SIGTERM);
}
/*
 * Do sb_commit()
 * @author: Jungmo Ahn
 */
enum _error_code_t do_sb_commit()
{
	enum _error_code_t ret;

	while(1) {
		pthread_mutex_lock(&mutex);
		ret = sb_commit();
		if(ret != SB_ERR_NONE) {
			printerror();
		}
		pthread_mutex_unlock(&mutex);
		sleep(5);
	}
}
/* Do sb_update()
 * @author: Jungmo Ahn
 */

enum _error_code_t do_sb_update()
{
	enum _error_code_t ret;

	while(1) {
		pthread_mutex_lock(&mutex);
		ret = sb_update();
		if(ret != SB_ERR_NONE) {
			printerror();
		}
		pthread_mutex_unlock(&mutex);
		sleep(5);
	}
}

int main(int argc, char** argv)
{
	int			vcs = 1;
	enum _error_code_t	ret = SB_ERR_NONE;
	int			status = 0;

	ret = do_sb_init(vcs, dir);
	if(ret != SB_ERR_NONE) {
		printerror(ret);
	}	

	//TODO:modify parameters of add, remove
	ret = sb_add(dir);
	if(ret != SB_ERR_NONE) {
		printerror(ret);
	}
	
	ret = sb_remove(dir);
	if(ret != SB_ERR_NONE) {	
		printerror(ret);
	}	

	pthread_join(thread_id[THREAD_COMMIT], (void *) &status);
	pthread_join(thread_id[THREAD_UPDATE], (void *) &status);
	return 0;
}
