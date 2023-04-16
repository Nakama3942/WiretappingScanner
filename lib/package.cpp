#include "package.hpp"

__declspec(dllexport)
unsigned char * packaging(int *data, int size)
{
	unsigned char *packet = new unsigned char[size * 4];
	asm(
		"1:\n"
		"movl (%1), %%eax\n" // сохраняем элемент в 4 байта блока памяти
		"bswap %%eax\n"      // меняем порядок байтов в eax
		"movl %%eax, (%0)\n" // записываем байты сохранённого элемента
		"add $4, %1\n"       // переходим к следующему слову для следующего цикла
		"add $4, %0\n"       // переходим к следующему слову для следующего цикла
		"dec %2\n"           // пока не обработаем все 10 слов, ...
		"jnz 1b\n"           // ... повторяем цикл
		:
		: "r" (packet), "r" (data), "r" (size)
		: "eax", "memory"
	);
	return packet;
}

__declspec(dllexport)
int * unpackaging(unsigned char *packet, int size)
{
	size /= 4;
	int *data = new int[size];
	asm(
		"1:\n"
		"movl (%1), %%eax\n" // сохраняем элемент в 4 байта блока памяти
		"bswap %%eax\n"      // меняем порядок байтов в eax
		"movl %%eax, (%0)\n" // записываем байты сохранённого элемента
		"add $4, %1\n"       // переходим к следующему слову для следующего цикла
		"add $4, %0\n"       // переходим к следующему слову для следующего цикла
		"dec %2\n"           // пока не обработаем все 10 слов, ...
		"jnz 1b\n"           // ... повторяем цикл
		:
		: "r" (data), "r" (packet), "r" (size)
		: "eax", "memory"
	);
	return data;
}
