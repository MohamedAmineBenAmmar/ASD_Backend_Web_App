#include "../dictionary/dictionary_functions.h"


int main(int argc, char **argv)
{
    buildDictFromFile(argv[1], argv[2]);
    return 0;
}