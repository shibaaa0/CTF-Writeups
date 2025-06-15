
undefined8 win1(void)

{
  int iVar1;
  undefined8 uVar2;
  char local_28 [23];
  char local_11;
  FILE *local_10;
  
  puts("You have passed the first challenge. The next one won\'t be so simple.");
  printf("Lesson 2 Arguments: Research how arguments are passed to functions and apply your learning. Bring the artifact of 0xDEADBEEF to the temple of %p to claim your advance."
         ,win2);
  local_10 = fopen("flag1.txt","r");
  if (local_10 == (FILE *)0x0) {
    perror("Error opening file");
    uVar2 = 1;
  }
  else {
    while( true ) {
      iVar1 = fgetc(local_10);
      local_11 = (char)iVar1;
      if (local_11 == -1) break;
      putchar((int)local_11);
    }
    fclose(local_10);
    local_28[0] = '\0';
    local_28[1] = '\0';
    local_28[2] = '\0';
    local_28[3] = '\0';
    local_28[4] = '\0';
    local_28[5] = '\0';
    local_28[6] = '\0';
    local_28[7] = '\0';
    local_28[8] = '\0';
    local_28[9] = '\0';
    local_28[10] = '\0';
    local_28[0xb] = '\0';
    local_28[0xc] = '\0';
    local_28[0xd] = '\0';
    local_28[0xe] = '\0';
    local_28[0xf] = '\0';
    puts("Continue: ");
    fgets(local_28,0x60,stdin);
    uVar2 = 0;
  }
  return uVar2;
}

