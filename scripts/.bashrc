[[ $- != *i* ]] && return

cb() {
	
	tmpFile=$(shuf -i 100000-1000000 -n 1)
	mkdir /tmp/cpp -p
	g++ $1 -o /tmp/cpp/tmp$"$tmpFile"bin
       	if [ $? == 0 ]; then
		/tmp/cpp/tmp$"$tmpFile"bin
		rm /tmp/cpp/tmp$"$tmpFile"bin
	fi
}
export HISTCONTROL=ignoreboth
alias eww='~/eww/target/release/eww'
fastfetch --kitty ~/image.jpg --logo-height 25 --logo-recache
