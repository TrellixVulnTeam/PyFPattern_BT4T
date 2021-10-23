def setUp(self):
    super(OrganizationDiscoverTest, self).setUp()
    self.user = self.create_user('foo@example.com')
    self.org = self.create_organization(owner=None, name='Rowdy Tiger')
    self.team = self.create_team(organization=self.org, name='Mariachi Band')
    self.create_member(user=self.user, organization=self.org, role='owner', teams=[self.team])
    self.project = self.create_project(organization=self.org, teams=[self.team], name='Bengal')
    self.group = self.create_group(project=self.project)
    self.event = self.create_event(group=self.group, message='message!', platform='python')
    self.login_as(self.user)
    self.path = '/organizations/{}/discover/'.format(self.org.slug)