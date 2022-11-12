def validator_rc(rodne_cislo):
    """
    :param rodne_cislo zadané jako str s nebo bez "/"
    :return: True v případě platnosti RČ a False v případě neplatnosti RČ
    """
    rc_v_listu = []

    for cislice in rodne_cislo:
        if cislice.isdigit():
            rc_v_listu += cislice

    rok_narozeni = int(rc_v_listu[0] + rc_v_listu[1])
    mesic_narozeni = int(rc_v_listu[2] + rc_v_listu[3])
    den_narozeni = int(rc_v_listu[4] + rc_v_listu[5])
    unor = [2, 52]
    mesice_30_dnu = [4, 6, 9, 11, 54, 56, 59, 61]
    mesice_31_dnu = [1, 3, 5, 7, 8, 10, 12, 51, 53, 55, 57, 58, 60, 62]

    if len(rc_v_listu) == 10 and 3 < rok_narozeni < 54:
        unor.extend([22, 72])
        mesice_30_dnu.extend([24, 26, 29, 31, 74, 76, 79, 81])
        mesice_31_dnu.extend([21, 23, 25, 27, 28, 30, 32, 71, 73, 75, 77, 78, 80, 82])

    if mesic_narozeni not in unor and mesic_narozeni not in mesice_30_dnu and mesic_narozeni not in mesice_31_dnu:
        return False

    if mesic_narozeni in mesice_30_dnu and den_narozeni > 30:
        return False

    if mesic_narozeni in mesice_31_dnu and den_narozeni > 31:
        return False

    if mesic_narozeni in unor:
        if rok_narozeni % 4 != 0 and den_narozeni > 28:
            return False
        elif rok_narozeni % 4 == 0 and den_narozeni > 29:
            return False

    if len(rc_v_listu) == 9:
        if rok_narozeni > 53:
            return False
        elif rc_v_listu[-3:] == ["0", "0", "0"]:
            return False
        else:
            return True

    elif len(rc_v_listu) == 10:
        prvnich_10_cisel_rc = rc_v_listu.copy()
        prvnich_10_cisel_rc.pop()
        pomocne_rc = ""

        for cislice in prvnich_10_cisel_rc:
            pomocne_rc += cislice

        kontrolni_cislice = int(pomocne_rc) % 11

        if kontrolni_cislice != int(rc_v_listu[-1]):
            if kontrolni_cislice == 10 and int(rc_v_listu[-1] != 0):
                return False
            return False
        else:
            return True
    else:
        return False
