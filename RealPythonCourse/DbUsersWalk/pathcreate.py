import os
import sys
import getopt


def main(argv):
    cpaneluser = ''
    cms = ''

    def wp_change_passwords():
        cp_path = os.path.join('/home/', cpaneluser)
        print cp_path

    try:
        opts, args = getopt.getopt(argv, "c:p:", ["cpanel=", "cms="])
    except getopt.GetoptError:
        print 'No such option.'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'help'
            sys.exit()
        elif opt in ("-c", "--cpanel"):
            cpaneluser = arg
        elif opt in ("-", "--cms"):
            cms = arg
            if cms == 'wordpress':
                wp_change_passwords()


if __name__ == "__main__":
    main(sys.argv[1:])

