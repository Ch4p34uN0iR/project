#!/bin/bash

CHECKING=`apt update 2>/dev/null`

function logme() {
	for account in me you and mom; do
		printf "`date`: $1\n" >> /home/$account/HashcatLogging.txt
	done
}

if [[ $CHECKING != *"can be upgraded"* ]] ; then
	MESSAGE=`printf "No updates are available\n"`
	logme "$MESSAGE"
else
	MESSAGE=`printf "$CHECKING" | grep "can be upgraded" | cut -d "." -f 1 | sed "s/can be/were/"`
	apt upgrade -y || logme "Uh-oh! Something went wrong upgrading!"
	apt dist-upgrade -y || logme "Uh-oh! Something went wrong with dist-upgrade!"
	apt autoremove -y || logme "Uh-oh! Something went wrong with autoremoving!"
	logme "$MESSAGE"
fi
