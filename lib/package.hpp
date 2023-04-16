#ifndef PACKAGE_HPP
#define PACKAGE_HPP

#include "package_global.hpp"

#ifdef __cplusplus
extern "C" {
#endif

extern "C" __declspec(dllexport)
unsigned char *packaging(int *data, int size);
extern "C" __declspec(dllexport)
int *unpackaging(unsigned char *packet, int size);

#ifdef __cplusplus
}
#endif

#endif // PACKAGE_HPP
