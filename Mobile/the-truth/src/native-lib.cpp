#include <jni.h>
#include <string>

extern "C" JNIEXPORT jstring JNICALL
Java_com_csc_thetruth_TruthChecker_TheTruth(
        JNIEnv* env,
        jobject /* this */) {
    std::string Truth = "uI2^uStUI^h4^ui2^M0Fiu^uI5u^V0mM^FT0ehOf^X1T^G1sV5sE";
    return env->NewStringUTF(Truth.c_str());
}