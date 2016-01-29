/*
 * SetupBox_test.c
 * This program is written for testing  SetupBox's function such as
 * sb_init(), sb_destory(), sb_update(), sb_commit(), sb_add(), sb_remove().
 * 
 * Autor:	Jungmo Ahn <ajm100@ajou.ac.kr>
 *
 */
#include <stdio.h>
#include <string.h>
#include "CUnit/Basic.h"
#include "vcscontroller.h"

#define DIR "blah blah"

/*
 * To initialize a suite.
 * @author: Jungmo Ahn
 * @return: return 0 on success, non-zero otherwise.
 * @todo: set a file to test.
 */
int init_suite(void)
{

}

/*
 * To clean up a suite.
 * @author: Jungmo Ahn
 * @return: return 0 on success, non-zero otherwise.
 * @todo: delete all of information.
 */
int clean_suite(void)
{

}

/*
 * Testing sb_init(enum VCS vcs, const char* dir)
 * @author: Jungmo Ahn
 * @todo: write test code
 */
void testINIT(void)
{
	CU_ASSERT(sb_init(0, DIR));	
}

/*
 * Testing sb_destroy()
 * @author: Jungmo Ahn
 * @todo: write test code.
 */
void testDESTROY(void)
{
	CU_ASSERT(sb_destory());
}

/*
 * Testing sb_update()
 * @author: Jungmo Ahn
 * @todo: write test code.
 */
void testUPDATE(void)
{
	CU_ASSERT(sb_update());
}

/*
 * Testing sb_commit()
 * @author: Jungmo Ahn
 * @todo: write test code.
 */
void testCOMMIT(void)
{
	CU_ASSERT(sb_commit());
}

/*
 * Testing sb_add()
 * @author: Jungmo Ahn
 * @todo: write test code.
 */
void testADD(void)
{
	CU_ASSERT(sb_ad());
}

/*
 * Testing sb_remove()
 * @author: Jungmo Ahn
 * @todo: write test code.
 */
void testREMOVE(void)
{
	CU_ASSERT(sb_remove());
}

/*
 * @author: Jungmo Ahn
 * @return: return 0 on success, non-zero otherwise.
 * @todo: main.
 */
int main()
{
	CU_pSuite pSuite = NULL;

	// Initiailze the CUnit test registry.
	if(CUE_SUCCESS != CU_initialize_registry())
		return CU_get_error();
	
	// Add a suite to the registry.
	pSuite = CU_add_suite("Suite", init_suite, clean_suite);
	
	if(NULL = pSuite) {
		CU_cleanup_registry();
		return CU_get_error();
	}

	// Add the test to the suite.
	// TODO: Consider an order of functions after adding OTHER functions.
	if ((NULL == CU_add_test(pSuite, "test of sb_init()", testINIT))) {
		CU_cleanup_registry();
		return CU_get_error();
	}

	CU_basic_set_mode(CU_BRM_VERBOSE);
	CU_basic_run_tests();
	CU_cleanup_registry();
	
	return CU_get_error();
	
}
