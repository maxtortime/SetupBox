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

#define THREAD_UPDATE 0
#define THREAD_COMMIT 1
#define THREAD_TOTAL 2

char dir[256];

int thread_id[THREAD_TOTAL];
pthread_t thread[THREAD_TOTAL];

/*
 * Initialize a thread for running sb_update()
 * @author: Jungmo Ahn
 * @return: return 0 on success, non-zero otherwise.
 * @todo: Specifying what parameter is needed for sb_update
 *        now, it sets NULL(fourth parameter).
 */
enum _error_code_t do_sb_update()
{
	// enum _error_code_t ret;
	thread_id[THREAD_UPDATE] = pthread_create(&thread_id[THREAD_UPDATE], NULL, sb_update, NULL);
}

/*
 * Initialize a thread for running sb_commit()
 * @author: Jungmo Ahn
 * @return: return 0 on success, non-zero otherwise.
 * @todo: Specifying what parameter is needed for sb_update
 * 	  now, it sets NULL(fourth parameter).
 */

enum _error_code_t do_sb_commit()
{
	thread_id[THREAD_COMMIT] = pthread_create(&thread[THREAD_COMMIT], NULL, sb_commit, NULL);
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
	
	sprintf(dir, "%s/.SetupBox",getenv("HOME"));
	
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

void showerror(enum _error_code_t ret)
{
	// if there is an error, terminate SetupBox
	printf("error occurs. error code : %d\n", ret);
	exit(15);
}

int main(int argc, char** argv)
{
	int vcs = 1;
	enum _error_code_t ret = SB_ERR_NONE;


	ret = do_sb_init(vcs, dir);
	if(ret != SB_ERR_NONE) {
		showerror(ret);
	}	
	
	ret = do_sb_update();
	if(ret != SB_ERR_NONE) {
		showerror(ret);
	}
	
	ret = do_sb_add();
	if(ret != SB_ERR_NONE) {
		showerror(ret);
	}
	
	ret = do_sb_remove();
	if(ret != SB_ERR_NONE) {	
		showerror(ret);
	}	

	ret = do_sb_commit();
	if(ret != SB_ERR_NONE) {
		showerror(ret);
	}	
	return 0;

}
