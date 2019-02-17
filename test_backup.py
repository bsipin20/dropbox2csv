import unittest
import dropbox
import ex_backup 

TOKEN= "5a5bbxKLU_wAAAAAAACNDrmiKz-YfnPds9iy-N-DeY0QTJRdo9_GOYS17Qn1Fcx_"
LOCALFILE = 'my-file.txt'
BACKUPPATH = '/my-file-backup.txt'


class TestBackup(unittest.TestCase):

    ex_backup.dbx = dropbox.Dropbox(TOKEN)


    def test_restore(self):
        ex_backup.select_revision()
        ex_backup.backup()


 
        



if __name__ == '__main__':
    unittest.main()
