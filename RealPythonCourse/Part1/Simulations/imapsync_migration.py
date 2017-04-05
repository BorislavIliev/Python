emails = ['albena.ilieva@mgas-bg.com',
'anelia.todorova@mgas-bg.com',
'boriana.manolova@mgas-bg.com',
'borislav.savchev@mgas-bg.com',
'denica.ruseva@mgas-bg.com',
'dima.ignatova@mgas-bg.com',
'georgi.hristov@mgas-bg.com',
'georgi.iliev@mgas-bg.com',
'gergana.manolova@mgas-bg.com',
'ihtiman@mgas-bg.com',
'iliana.iordanova@mgas-bg.com',
'iskren.isaev@mgas-bg.com',
'ivan.mihov@mgas-bg.com',
'jivko.stamatov@mgas-bg.com',
'julia.toleva@mgas-bg.com',
'jumbo@mgas-bg.com',
'miglena.kostova@mgas-bg.com',
'office@mgas-bg.com',
'rosica.kopcheva@mgas-bg.com',
'stoqn.manolov@mgas-bg.com']

password = 'MmGg@aSs234987?!'

for i in emails:
    print('imapsync --host1 mail.mgas-bg.com --user1 {0} --password1 {1} --noauthmd5  LOGIN --host2 mx01.cmailpro.net --user2 {0} --password2 {1} --noauthmd5 LOGIN --skipsize --allowsizemismatch'.format(i, password,))

for i in emails:
    print('dommailadd {0} {1}'.format(i, password))