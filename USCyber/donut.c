
/* WARNING: Unknown calling convention -- yet parameter storage is locked */

void maintenance(void)

{
  long lVar1;
  long in_FS_OFFSET;
  char cmd [100];
  
  lVar1 = *(long *)(in_FS_OFFSET + 0x28);
  if (donuts == -0x35014542) {
    puts("Welcome to the admin panel!");
    puts("Date:");
    snprintf(cmd,100,"date --date=\'TZ=\"%s\"\'",timezone);
    system(cmd);
    puts("What would you like to set your balance to?");
    printf("> ");
    __isoc99_scanf(&DAT_0010204a,&money);
    puts("Balance set!");
  }
  else {
    puts("You aren\'t authorized to access this!");
  }
  if (lVar1 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

