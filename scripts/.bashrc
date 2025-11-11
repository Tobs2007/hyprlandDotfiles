[[ $- != *i* ]] && return

cb() {
	
	tmpFile=$(shuf -i 100000-1000000 -n 1)
	mkdir /tmp/cpp -p
	g++ $1 -o /tmp/cpp/tmp$"$tmpFile"bin
       	result=$?
	if [ $result == 0 ]; then
		/tmp/cpp/tmp$"$tmpFile"bin
		result=$?
		rm /tmp/cpp/tmp$"$tmpFile"bin
	fi
	return $result
}
export HISTCONTROL=ignoreboth
alias eww='~/eww/target/release/eww'

[[ $TERM_PROGRAM != "vscode" ]] && fastfetch --kitty ~/image.jpg --logo-height 25 --logo-recache
