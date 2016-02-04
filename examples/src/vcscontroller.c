/*
 * TODO please put GPL license stuff.
 * vcscontroller.h
 *
 * Author: 	Jaewon Choi <jainersoer@gmail.com>
 * 			Jungmo Ahn	<ajm100@ajou.ac.kr>
 */


#include "vcscontroller.h"

static struct 
{
}_sb_vcs_context;

error_code_t sb_init(enum VCS vcs, const char* dir)
{
}

error_code_t sb_destroy()
{
}

// ASSUME: Currently, there exists "one" unique repo.
error_code_t sb_update()
{
}

error_code_t sb_commit()
{
}

/*
 * @author: Jaewon Choi, Jungmo Ahn
 * @param: const char* target
 * 	It's Okay whether target is a file or directory.
 * @todo: please add a comment like this to all functions.
 */
error_code_t sb_add(const char* target)
{
}

/*
 * @author: Jaewon Choi, Jungmo Ahn
 * @param: const char* target
 * 	It's Okay whether target is a file or directory.
 * @todo: please add a comment like this to all functions.
 */
error_code_t sb_remove(const char* target)
{
}


