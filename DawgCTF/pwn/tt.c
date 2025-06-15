
/* WARNING: Unknown calling convention -- yet parameter storage is locked */
/* handleOption() */

void handleOption(void)

{
  bool bVar1;
  __uid_t _Var2;
  long *plVar3;
  ostream *poVar4;
  long in_FS_OFFSET;
  int local_5d4;
  int local_5d0;
  int local_5cc;
  string local_5c8 [32];
  istringstream local_5a8 [384];
  int local_428 [258];
  long local_20;
  
  local_20 = *(long *)(in_FS_OFFSET + 0x28);
  local_5d0 = 0;
  std::string::string(local_5c8);
                    /* try { // try from 0010171b to 0010173d has its CatchHandler @ 0010192b */
  std::getline<>((istream *)std::cin,local_5c8);
  std::istringstream::istringstream(local_5a8,local_5c8,8);
  while( true ) {
    plVar3 = (long *)std::istream::operator>>((istream *)local_5a8,&local_5d4);
    bVar1 = std::ios::operator_cast_to_bool((ios *)((long)plVar3 + *(long *)(*plVar3 + -0x18)));
    if ((bVar1) && (local_5d0 < 0x100)) {
      bVar1 = true;
    }
    else {
      bVar1 = false;
    }
    if (!bVar1) break;
    if ((local_5d4 < 1) || (3 < local_5d4)) {
                    /* try { // try from 00101789 to 001018b5 has its CatchHandler @ 00101913 */
      poVar4 = std::operator<<((ostream *)std::cout,"Ignoring invalid option: ");
      poVar4 = (ostream *)std::ostream::operator<<(poVar4,local_5d4);
      std::ostream::operator<<(poVar4,std::endl<>);
    }
    else {
      local_428[local_5d0] = local_5d4;
      local_5d0 = local_5d0 + 1;
    }
  }
  if ((local_428[0] == 2) && (_Var2 = geteuid(), _Var2 != 0)) {
    bVar1 = true;
  }
  else {
    bVar1 = false;
  }
  if (bVar1) {
    poVar4 = std::operator<<((ostream *)std::cout,"Error: Option 2 requires root privileges HAHA");
    std::ostream::operator<<(poVar4,std::endl<>);
  }
  else {
    for (local_5cc = 0; local_5cc < local_5d0; local_5cc = local_5cc + 1) {
      if (local_428[local_5cc] == 1) {
        sayHello();
      }
      else if (local_428[local_5cc] == 2) {
        printFlag();
      }
      else if (local_428[local_5cc] == 3) {
        login();
      }
    }
  }
  std::istringstream::~istringstream(local_5a8);
  std::string::~string(local_5c8);
  if (local_20 == *(long *)(in_FS_OFFSET + 0x28)) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

