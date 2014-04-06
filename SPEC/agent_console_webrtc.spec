%define modname video_agent_console_webrtc
Summary: Elastix Module agent_console_webrtc
Name: elastix-%{modname}
Version: 0.1
Release: 1
License: GPLv3
Group: Applications/System
Source0: elastix-agent_console_webrtc-0.1.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildArch: noarch
Prereq: screen perl-WWW-Curl elastix-callcenter libtool >= 2.4.2-DMv1 libsrtp >= 1.4.5-DMv1  yasm >= 1.2.0-DMv1 libvpx >= 1.2.0-DMv1 x264 >= snapshot20130810.2245-DMv1 ffmpeg >= 1.2-DMv1 doubango >= 2.0r95 webrtc2sip >= 2.4.5r114-DMv1

%description
Add and Adapt the agent console to use the SIPML5 API, to provide a softphone and chat service in the agent console.developed by digital-merge. More Info at www.digital-merge.com or info@digital-merge.com

%prep

%setup -n %{modname}

%install
rm -rf $RPM_BUILD_ROOT

# Files provided by all Elastix modules
mkdir -p $RPM_BUILD_ROOT/var/www/html/
mv modules/ $RPM_BUILD_ROOT/var/www/html/

# The following folder should contain all the data that is required by the installer,
# that cannot be handled by RPM.
mkdir -p $RPM_BUILD_ROOT/usr/share/elastix/module_installer/%{name}-%{version}-%{release}/
mv setup/ $RPM_BUILD_ROOT/usr/share/elastix/module_installer/%{name}-%{version}-%{release}/
mv menu.xml $RPM_BUILD_ROOT/usr/share/elastix/module_installer/%{name}-%{version}-%{release}/

%pre
mkdir -p /usr/share/elastix/module_installer/%{name}-%{version}-%{release}/	  
touch /usr/share/elastix/module_installer/%{name}-%{version}-%{release}/preversion_%{modname}.info
if [ $1 -eq 2 ]; then
rpm -q --queryformat='%{VERSION}-%{RELEASE}' %{name} > /usr/share/elastix/module_installer/%{name}-%{version}-%{release}/preversion_%{modname}.info
fi

%post

pathModule="/usr/share/elastix/module_installer/%{name}-%{version}-%{release}"

# Run installer script to fix up ACLs and add module to Elastix menus.
elastix-menumerge $pathModule/menu.xml
pathSQLiteDB="/var/www/db"
mkdir -p $pathSQLiteDB
preversion=`cat $pathModule/preversion_%{modname}.info`
if [ $1 -eq 1 ]; then #install
# The installer database
elastix-dbprocess "install" "$pathModule/setup/db"


elif [ $1 -eq 2 ]; then #update
elastix-dbprocess "update" "$pathModule/setup/db" "$preversion"
fi


%clean
rm -rf $RPM_BUILD_ROOT

%preun
if [ $1 -eq 0 ] ; then # Validation for desinstall this rpm
echo "Delete example menus"
elastix-menuremove "%{modname}"

# Here you should call to elastix-dbprocess for deleting, the same waythat it was for install, just that instead of word “install” goes word“delete”. But this is not often used due to the databases usually are not deleted
/bin/sed -i '/;----------Handler to send & receive sip message for agent console/,/;----------End Handler to send & receive sip message for agent console/d' /etc/asterisk/extensions_custom.conf

fi

%files
%defattr(-, asterisk, asterisk)
%{_localstatedir}/www/html/*
/usr/share/elastix/module_installer/*

