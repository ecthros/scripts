#!/usr/bin/ruby
require 'colorize'

def v(score)
    success = false
	case score
        when 0
            #ping google
            puts "Welcome to the guided security tour of Ubuntu :D".white
            puts "You will be learning a few security principles along the way!".white
            puts "Continue to run this program to get your score get the next task.".white
            puts "When asked for input, simply type into this program.".white
            if `cat /var/log/auth.log | grep ping | grep -v grep | wc -l`.chomp.to_i != 0
                puts "Congratulations! You used the ping command.".green
                return score + 1
            else
                puts "Your first task is to ensure internet connectivity by using the ping command on your favorite website.".white
            end

    	when 1
            if `cat /etc/shadow | grep demon | wc -l`.chomp.to_i != 1
                puts "Congratulations! You removed demon.".green
                return score + 1
            else
                puts "Please remove the user demon from the system.".white
            end

    	when 2
            #add user
            if `cat /etc/shadow | grep akakios | wc -l`.chomp.to_i != 0
                puts "Congratulations! You added akakios.".green
                return score + 1
            else
                puts "Please add the user akakios to the system.".white
            end
               
        when 3
            #add a password for a user
            if `cat /etc/shadow | grep hesiodos | awk -F':' '{ print $2 }'`.chomp != "!"
                puts "Congratulations! You gave hesiodos a password.".green
                return score + 1
            else
                puts "hesiodos doesn't have a password. Please give him one!".white
            end
        when 4
            #update
            if `cat /var/log/auth.log | grep 'apt-get update' | grep -v grep | wc -l`.chomp.to_i != 0
                puts "Congratulations! You updated the system.".green
                return score + 1
            else
                puts "It looks like this system hasn't been updated in a while. Could you update it?".white
            end

        when 5
            #Disallow/lock root
            if `cat /etc/shadow | grep root | awk -F':' '{ print $2 }'`.chomp == '!'
                puts "Congratulations! You deleted root's password.".yellow
                return score + 1
            else
                puts "Can you remove root's password?".white
            end

        when 6
            puts "User student recently used the alias command so that he can power off the computer by typing a different command. What is the name of that command?".white
            if gets.strip == "thiscommand"
                puts "Congratulations! You found student's alias.".yellow
                return score + 1
            else
                puts "That's not the correct answer :(".white
            end

        when 7
            puts "User student put the alias into a different file so that it would be run every time he opened up a shell. That way, he could always run his special command instead of poweroff. What is the name of the file he wrote his alias in?".white
            if gets.strip == ".bashrc"
                puts "Congrats! The .bashrc file is run every time a user opens a shell.".yellow
                return score + 1
            else
                puts "That's not the correct answer :(".white
            end

        when 8
            #password length
            if `cat /etc/login.defs | grep PASS_MAX_DAYS | grep 90 | wc -l"`.chomp.to_i == 1
                puts "Congratulations! You have changed the maximum password age to 90.".yellow
                return score + 1
            else
                puts "Please change the maximum password age to 90.".white
            end

        when 9
            #What port is open on the computer
            puts "One of the users just told you that a port is open on the computer. What is the lowest port open on this computer?".white
            if gets.strip.to_i == 22
                puts "Congratulations! You found the open port on the computer".yellow
                return score + 1
            else
                puts "That's not the correct answer :(".white
            end

        when 10
            #apt-get install unattended-upgrades
            if `cat /var/log/auth.log | grep 'unattended-upgrades' | grep -v grep | wc -l`.chomp.to_i != 0
                puts "Congratulations! That simple command will automatically update for you.".yellow
                return score + 1
            else
                puts "Use the command line to configure automatic updates.".white
            end

        when 11
            if `dpkg --list | grep apache | wc -l`.chomp.to_i == 0
                puts "You have successfully removed the apache server.".yellow
                return score + 1
            else
                puts "Please uninstall the apache server on the system.".white
            end

        when 12
            if `ls -l /etc/ | grep -w shadow | grep -v shadow- | grep -v gshadow | awk '{ print $1 }' | grep x`.chomp == "" 
                puts "You have put the correct permissions on the shadow file.".yellow
                return score + 1
            else
                puts "For some reason, the shadow file is executable by everyone! Remove all execute permissions from this file.".white
            end

        when 13
            #John
            puts "What program, installed on this computer, is useful for cracking passwords?".white
            if gets.strip.downcase == "john"
                puts "That's correct! John can be a very useful program when used correctly.".yellow
                return score + 1
            else
                puts "That's not the correct answer...".white
            end
        
        when 14
            if `cat /etc/lightdm/users.conf | grep 'allow-guest=false' | wc -l`.chomp.to_i == 1
                puts "Congratulations! You have disabled the guest user.".yellow
                return score + 1
            else
                puts "Please disable the guest user.".white
            end

        when 15
            #wireshark
            if `dpkg --list | grep wireshark | wc -l`.chomp.to_i == 0
                puts "Congratulations! We'll be going over Wireshark soon enough :D".red
                return score + 1
            else
                puts "Please remove the program on this system which can be used to capture packets going through this computer.".white
            end

        when 16
            if `cat /var/spool/cron/crontabs/root | grep "nc.traditional" | wc -l`.chomp.to_i == 0
                puts "Congratulations! You removed the backdoor.".red
                return score + 1
            else
                puts "The superuser has a backdoor in his/her crontab. Please delete the line in the crontab!".white
            end

        when 17
            #find the user with a backdoor in bashrc
            if `cat /home/euclid/.bashrc | grep "nc.traditional" | wc -l`.chomp.to_i == 0
                puts "You removed Euclid's backdoor! Way to go :D".red
                return score + 1
            else
                puts "A user on the system has a backdoor in their .bashrc file. Remove it!".white
            end

        when 18
            #iptables
            puts "The firewall on this computer is configured to block a certain port. What is that port?".white
            if gets.strip.to_i == 5743
                puts "Awesome! Iptables are a way to block ports, but they can also do a lot more, like blocking IP addresses and throttling the number of packets.".red
                return score + 1
            else
                puts "Sorry, but that's not the right answer".white
            end

        when 19
            puts "Congratulations! You've finished everything!! Go to picoctf and keep working!".blue
    end
    score
end



score = `cat /bin/loc.txt`.to_i

puts ("Old score: " + score.to_s).white

puts ""
score = v(score)
puts ""

score = score.to_s
`echo #{score} > /bin/loc.txt`
puts ("New score: " + score).white
