import dotbot


class Restore(dotbot.Plugin):
    '''
    BRAINSTORMING RESTORE PLUGIN FUNCTIONALITY

    - restore:
        clean:  # indicates if we want to remove the backup files after restoring them. False by default
        replace:  # do we need this? indicates if we want to replace existing files. isn't that the point of a restore?
        force:  # maybe we want force instead of replace to indicate force replacing FILES, not just links
        exclude:  # list of files to exclude in the restore, must be the dotfile path
        files:  # list of the files to include in the restore - will not restore any others outside this list
        # if neither exclude nor files is used, then it will be a full restore for all backed up files

        otherwise, loops through the config to find the files that were backed up and where. 
        will work a lot like the Link plugin and lean on that process heavily
    
    make it possible to add this to the config without being run by default
    ./install --restore 
    should run the restore as indicated in the config, or a full restore if not indicated
    ./install --full-restore
    for a complete restore. should we accept other params to complete the experience just in the CLI, if desired?

    should this class inherit the Link plugin to take advantage of its functions? (probably)
    '''

    _directive = 'restore'

    def can_handle(self, directive):
        return directive == self._directive

    def handle(self, directive, data):
        if directive != self._directive:
            raise ValueError('Restore cannot handle directive %s' % directive)
        return self._process_restore(data)

    def _process_restore(self, data):
        # TODO
        return
