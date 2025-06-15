
undefined8 main(void)

{
  int iVar1;
  uint uVar2;
  size_t __n;
  long lVar3;
  ulong uVar4;
  char *pcVar5;
  undefined8 *puVar6;
  char *pcVar7;
  long in_FS_OFFSET;
  byte bVar8;
  int local_344;
  int local_340;
  int local_33c;
  undefined1 local_338 [16];
  undefined8 local_328;
  undefined4 local_318;
  undefined4 local_314 [8];
  char local_2f4 [267];
  char local_1e9 [8];
  uint local_1e1;
  char local_1dd [32];
  undefined8 local_1bd;
  undefined8 local_1b5;
  undefined8 local_1ad;
  undefined8 local_1a5;
  char local_198 [392];
  long local_10;
  
  bVar8 = 0;
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  puVar6 = (undefined8 *)&local_318;
  for (lVar3 = 0x2f; lVar3 != 0; lVar3 = lVar3 + -1) {
    *puVar6 = 0;
    puVar6 = puVar6 + 1;
  }
  *(undefined2 *)puVar6 = 0;
  *(undefined1 *)((long)puVar6 + 2) = 0;
  local_338 = (undefined1  [16])0x0;
  local_328 = 0;
  local_1e1 = 0;
  getrandom(&local_1e1,4,0);
  builtin_strncpy(local_2f4,"    .___",8);
  builtin_strncpy(local_1e9," 49   \n",8);
  pcVar5 = "    .____           __    __          \n    |    |    _____/  |__/  |_  ____  \n    |    |   /  _ \\   __\\   __\\/    \\ \n    |    |__(  <_> )  |  |  | (  <_> )\n    |_______ \\____/|__|  |__|  \\____/ \n            \\/                        \n    Enter 6 numbers in range 1 to 49   \n"
           + -(long)(local_2f4 + -(long)(local_2f4 + 4));
  pcVar7 = local_2f4 + 4;
  for (uVar4 = (ulong)((int)(local_2f4 + -(long)(local_2f4 + 4)) + 0x113U >> 3); uVar4 != 0;
      uVar4 = uVar4 - 1) {
    *(undefined8 *)pcVar7 = *(undefined8 *)pcVar5;
    pcVar5 = pcVar5 + ((ulong)bVar8 * -2 + 1) * 8;
    pcVar7 = pcVar7 + ((ulong)bVar8 * -2 + 1) * 8;
  }
  builtin_strncpy(local_1dd,"    Better luck next time ;)  \n",0x20);
  local_1bd = 0x626d754e20202020;
  local_1b5 = 0x6f6320666f207265;
  local_1ad = 0x7567207463657272;
  local_1a5 = 0x203a7365737365;
  setbuf(stdout,(char *)0x0);
  printf("%s\n    ",local_2f4);
  pcVar5 = local_198;
  for (lVar3 = 0x2f; lVar3 != 0; lVar3 = lVar3 + -1) {
    pcVar5[0] = '\0';
    pcVar5[1] = '\0';
    pcVar5[2] = '\0';
    pcVar5[3] = '\0';
    pcVar5[4] = '\0';
    pcVar5[5] = '\0';
    pcVar5[6] = '\0';
    pcVar5[7] = '\0';
    pcVar5 = pcVar5 + ((ulong)bVar8 * -2 + 1) * 8;
  }
  pcVar5[0] = '\0';
  pcVar5[1] = '\0';
  pcVar5[2] = '\0';
  fgets(local_198,0x17b,stdin);
  __n = strlen(local_198);
  memcpy(local_314,local_198,__n);
  srand(local_1e1);
  __isoc99_sscanf(local_314,"%u %u %u %u %u %u",local_338,local_338 + 4,local_338 + 8,
                  local_338 + 0xc,&local_328,(long)&local_328 + 4);
  for (local_344 = 0; local_344 < 6; local_344 = local_344 + 1) {
    iVar1 = rand();
    *(int *)(winingNumbers + (long)local_344 * 4) = iVar1 % 0x31 + 1;
  }
  for (local_340 = 0; local_340 < 6; local_340 = local_340 + 1) {
    *(int *)(userLookup + (ulong)*(uint *)(local_338 + (long)local_340 * 4) * 4) =
         *(int *)(userLookup + (ulong)*(uint *)(local_338 + (long)local_340 * 4) * 4) + 1;
    *(int *)(winingLookup + (ulong)*(uint *)(winingNumbers + (long)local_340 * 4) * 4) =
         *(int *)(winingLookup + (ulong)*(uint *)(winingNumbers + (long)local_340 * 4) * 4) + 1;
  }
  for (local_33c = 0; local_33c < 0x31; local_33c = local_33c + 1) {
    if ((*(int *)(userLookup + (long)local_33c * 4) != 0) &&
       (*(int *)(winingLookup + (long)local_33c * 4) != 0)) {
      uVar2 = *(uint *)(userLookup + (long)local_33c * 4);
      if (*(uint *)(winingLookup + (long)local_33c * 4) <=
          *(uint *)(userLookup + (long)local_33c * 4)) {
        uVar2 = *(uint *)(winingLookup + (long)local_33c * 4);
      }
      local_318 = uVar2 + local_318;
    }
  }
  if (local_318 == 6) {
    system("cat flag");
  }
  else {
    printf("%s%u\n",&local_1bd,(ulong)local_318);
    puts(local_1dd);
  }
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}

