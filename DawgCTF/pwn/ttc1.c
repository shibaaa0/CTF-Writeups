
undefined8 win2(int param_1)

{
  int iVar1;
  char local_38 [26];
  char local_1e [13];
  char local_11;
  FILE *local_10;
  
  if (param_1 != -0x21524111) {
    puts("You have failed to bring the artifact to the this temple. Return and try again");
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  sprintf(local_1e,"%X.txt",0xdeadbeef);
  puts(
      "You have done well, however you still have one final test. You must now bring 3 artifacts of [0xDEADBEEF] [0xDEAFFACE] and [0xFEEDCAFE]. You must venture out and find the temple yourself. I believe in you"
      );
  local_10 = fopen(local_1e,"r");
  if (local_10 == (FILE *)0x0) {
    perror("Error opening file");
  }
  else {
    while( true ) {
      iVar1 = fgetc(local_10);
      local_11 = (char)iVar1;
      if (local_11 == -1) break;
      putchar((int)local_11);
    }
    fclose(local_10);
    local_38[0] = '\0';
    local_38[1] = '\0';
    local_38[2] = '\0';
    local_38[3] = '\0';
    local_38[4] = '\0';
    local_38[5] = '\0';
    local_38[6] = '\0';
    local_38[7] = '\0';
    local_38[8] = '\0';
    local_38[9] = '\0';
    local_38[10] = '\0';
    local_38[0xb] = '\0';
    local_38[0xc] = '\0';
    local_38[0xd] = '\0';
    local_38[0xe] = '\0';
    local_38[0xf] = '\0';
    puts("Final Test: ");
    fgets(local_38,0x100,stdin);
  }
  return 1;
}

