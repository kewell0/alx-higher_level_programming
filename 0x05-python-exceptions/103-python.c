#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
 * print_python_float - prints some basic info about python floats
 * @p: pointer to PyObject object/float
 *
 * Return: no return value (void)
 */
void print_python_float(PyObject *p)
{
	printf("[.] bytes object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	else
	{
		printf("  value: %.9g\n", (((PyFloatObject *)(p))->ob_fval));
	}
}


/**
 * print_python_bytes - prints some basic info about python bytes
 * @p: pointer to PyObject object/list
 *
 * Return: no return value (void)
 */
void print_python_bytes(PyObject *p)
{
	long int size = 0, i = 0;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	else
	{
		printf("  size: %ld\n", (((PyVarObject *)(p))->ob_size));
		PyBytes_AsStringAndSize(p, &str, &size);
		printf("  trying string: %s\n", str);
		if (size < 10)
			printf("  first %ld bytes:", size + 1);
		else
			printf("  first 10 bytes:");
		for (i = 0; i <= size && i < 10; i++)
			printf(" %02hhx", str[i]);
		printf("\n");
	}
}

/**
 * print_python_list - prints some basic info about python lists
 * @p: pointer to PyObject object/list
 *
 * Return: no return value (void)
 */
void print_python_list(PyObject *p)
{
	PyObject *obj;
	long int i = 0, len = 0;

	if (PyList_Check(p))
	{
		len = ((PyVarObject *)(p))->ob_size;
		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %ld\n", len);
		printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

		while (i < len)
		{
			obj = PyList_GET_ITEM(p, i);
			printf("Element %ld: %s\n", i, (((PyObject *)(obj))->ob_type)->tp_name);
			i++;
			if (PyBytes_Check(((PyListObject *)obj)))
				print_python_bytes(((PyObject *)obj));
			if (PyFloat_Check(((PyListObject *)obj)))
				print_python_float(((PyObject *)obj));
		}
	}
}
