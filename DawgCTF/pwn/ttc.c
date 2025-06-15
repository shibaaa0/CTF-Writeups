
/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

undefined8 FUN_00401150(void)

{
  time_t tVar1;
  undefined8 local_38;
  undefined8 uStack_30;
  undefined8 local_28;
  undefined8 uStack_20;
  undefined4 local_18;
  
  tVar1 = time((time_t *)0x0);
  srand((uint)tVar1);
  puts("=== Frame Trap ===");
  puts("The bot is overwhelming... there\'s no fair way to win.");
  FUN_00401480();
  switch(DAT_004042c4) {
  case 0:
    break;
  case 1:
    goto switchD_004011ac_caseD_1;
  case 2:
    goto switchD_004011ac_caseD_2;
  case 3:
    goto switchD_004011ac_caseD_3;
  case 4:
    goto switchD_004011ac_caseD_4;
  default:
    return 0;
  }
switchD_004011ac_caseD_0:
  FUN_00401540(&local_38);
  DAT_004042c4 = 1;
  DAT_004042c0 = local_18;
  _DAT_004042a0 = local_38;
  uRam00000000004042a8 = uStack_30;
  _DAT_004042b0 = local_28;
  uRam00000000004042b8 = uStack_20;
  do {
    FUN_004014f0(&local_38);
    DAT_004042c4 = 2;
    DAT_00404280 = local_18;
    _DAT_00404260 = local_38;
    uRam0000000000404268 = uStack_30;
    _DAT_00404270 = local_28;
    uRam0000000000404278 = uStack_20;
switchD_004011ac_caseD_2:
    DAT_004042c8 = DAT_004042c8 + 1;
    __printf_chk(1,"\n[TURN %d]\n");
    __printf_chk(1,"Bot uses: %s\n",&DAT_00404260);
    __printf_chk(1,"You use: %s\n",&DAT_004042a0);
    DAT_004042c4 = 3;
switchD_004011ac_caseD_3:
    FUN_00401620();
    DAT_004042c4 = 4;
switchD_004011ac_caseD_4:
    if (0 < DAT_004040e0) {
      if (0 < DAT_004040a0) break;
      FUN_00401430();
    }
    FUN_00401460();
switchD_004011ac_caseD_1:
  } while( true );
  if (9 < DAT_004042c8) {
    puts(&DAT_00402390);
    DAT_004042c4 = 5;
    return 0;
  }
  DAT_004042c4 = 0;
  goto switchD_004011ac_caseD_0;
}

