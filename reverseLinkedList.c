#include <stdio.h>
#include <stdlib.h>

typedef struct node_t {
  int val;
  struct node_t *next;
} node;

node* newList( int* arr, int size ) {
  node* root = NULL;
  node* cp = NULL;
  node* pp = NULL;
  for( int i = 0; i < size; i++ ) {
    cp = ( node* )malloc( sizeof( node ));
    if( cp == NULL ){
      printf( "malloc failed.\n" );
      return NULL;
    }
    cp->val = arr[ i ];
    if( pp != NULL ) {
      pp->next = cp;
    }
    pp = cp;
    if( i == 0 ) {
      root = cp;
    }
  }
  return root;
}

void print( node* root ) {
  while( root != NULL ) {
    printf( "%d", root->val );
    root = root->next;
  }
  printf( "\n" );
}

void reverseList( node** root ) {
  if( root == NULL || *root == NULL ) {
    return;
  }
  node* np = *root;
  node* cp = *root;
  node* pp = NULL;
  while( np != NULL ) {
    if( np == cp ){
      np = np->next;
      continue;
    }
    cp->next = pp;
    pp = cp;
    cp = np;
    np = np->next;
  }
  cp->next = pp;
  *root = cp;
}

void freeList( node* root ) {
  if( root == NULL ) {
    return;
  }
  node* cp = root->next;
  node* pp = root;
  free( pp );
  while( cp != NULL ) {
    pp = cp;
    cp = cp->next;
    free( pp );
  }
}

void test( int* arr, int size ) {
  node* root = newList( arr, size );
  print( root );
  reverseList( &root );
  print( root );
  freeList( root );
}

int main(){
  int* a = NULL;
  test( a, 0 );
  // <<< XXX_TODO: need to account for newList, which doesn't default
  // node->next = NULL on instantiation.
  //int b[1] = { 0 };
  //test( b, 1 );
  int c[7] = { 0, 1, 2, 3, 4, 5, 6 };
  test( c, 7 );
  return 0;
}
