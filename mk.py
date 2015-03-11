#!/usr/bin/python 
import os, sys

ROOT="/media/e/android-ndk-r10d"
APPNAME=(os.path.abspath(".")).split("/")[-1].replace(".", "_")
NDK_PLATFORM_VER=8
CC="%s/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86/bin/arm-linux-androideabi-gcc" % ROOT
CPP="%s/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86/bin/arm-linux-androideabi-g++" % ROOT
INCLUDE="%s/platforms/android-%d/arch-arm/usr/include/"%(ROOT,NDK_PLATFORM_VER)
LIB="%s/platforms/android-%d/arch-arm/usr/lib"%(ROOT,NDK_PLATFORM_VER)
CFLAGS="-I %s"%INCLUDE
LDFLAGS="%s/crtbegin_dynamic.o %s/crtend_android.o -L %s -nostdlib -lc -lm -lgcc" % (LIB, LIB, LIB)
files=os.listdir("./")
cpp_files=[i for i in files if os.path.splitext(i)[-1] == ".cpp"]
c_files=[i for i in files if os.path.splitext(i)[-1] == ".c"]

if cpp_files:
  for i in cpp_files:
    os.system("%s -o %s -c %s %s"%(CPP, os.path.splitext(i)[0]+".o", i, CFLAGS))

if c_files:
  for i in c_files:
    os.system("%s -o %s -c %s %s"%(CC, os.path.splitext(i)[0]+".o", i, CFLAGS))

o_files=""

for i in files:
  if os.path.splitext(i)[-1] == ".o":
    o_files+=" %s" % i

if o_files:
  os.system("%s -o %s %s %s"%(CPP, APPNAME, o_files, LDFLAGS))

if len(sys.argv) > 1:
  if (sys.argv[1] == "push"):
    os.system("adb push %s /data/usr/%s" % (APPNAME, APPNAME))
#os.system("%s -o main.o -c main.cpp %s"%(CPP, CFLAGS))
#os.system("%s -o main main.o %s"%(CPP, LDFLAGS))