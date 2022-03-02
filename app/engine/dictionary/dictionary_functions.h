#ifndef DICTIONARY_FUNCTIONS_HEADER_FILE
#define DICTIONARY_FUNCTIONS_HEADER_FILE

#include "../tree/types.h"

/* -------------------------------------------------------*/ 
/* Primitives de gestion d’un dictionnaire */ 
/* -------------------------------------------------------*/ 
void dicoAfficher(TArbre a); 
void dicoInsererMot(char mot[], TArbre *pa); 
int dicoNbOcc(char mot[], TArbre a); 
int dicoNbMotsDifferents(TArbre a); 
int dicoNbMotsTotal(TArbre a); 

// Added functions
void buildDictFromFile(char filepath[], char destination_filepath[]); 
// void parseDict(TArbre a, char destination_file_path[]);
/* -------------------------------------------------------*/ 


#endif