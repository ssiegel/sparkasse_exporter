sparkasse-exporter
==================

The `Sparkasse+ Android
app <https://play.google.com/store/apps/details?id=com.starfinanz.smob.android.sbanking>`__
does not provide any export functionality, thus effectively “locking in”
long time users who don't want to lose their data.

This script allows exporting the data from a Sparkasse+ backup file to a
format called `SUPA <https://subsembly.com/supa.html>`__, which is a
simple TSV format ready to be imported by Subsembly's `Banking
4A <https://play.google.com/store/apps/details?id=subsembly.banking>`__
app. The file is simple enough to be converted to other formats easily,
and the script can be adapted as well.

It is currently unknown if the conversion works for backup files of the
free
`Sparkasse <https://play.google.com/store/apps/details?id=com.starfinanz.smob.android.sfinanzstatus>`__
or the
`StarMoney <https://play.google.com/store/apps/details?id=com.starfinanz.smob.android.starmoney>`__
apps as well, but it might work.

The conversion was successfully tested using real world data from about
five years and several accounts, about 3000 transaction records in
total.

Usage
-----

::

    sparkasse-exporter [-h] [-a IBAN] [-p PASSWORD] FILE

    Export transactions of a Sparkasse+ backup file to Subsembly SUPA format.

    positional arguments:
      FILE                  Sparkasse+ backup file to be converted

    optional arguments:
      -h, --help            show this help message and exit
      -a IBAN, --account IBAN
                            Only export records of account IBAN
      -p PASSWORD, --password PASSWORD
                            Password for opening the backup file

The script expects the backup file as argument. If no password is
provided, you will be asked for it. Please be aware that providing the
password on the command line poses a security risk. The conversion can
optionally be restricted to a specified account (any SQL LIKE pattern
will in fact work).

The converted records will be output to standard output in ISO 8859-1
encoding (mandated by the SUPA specification).
