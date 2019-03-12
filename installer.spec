%define name berry-installer
%define version 0.35
%define release b1

Name:		%{name}
Summary:	Berry Linux Installer
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Tools
Source:		%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}
#Requires:	lilo Xdialog
BuildArchitectures: noarch

%description
berry-installer is a small dialog-based script for installing
BERRY on a harddisk partition.


## Setup Section
%prep
%setup -q

## Build Section
%build

## Install Section
%install
mkdir -p %{buildroot}/opt/berry
mkdir -p %{buildroot}/opt/berry/modules/{booting,install}
install -m 755 berry-installer %{buildroot}/opt/berry
#install -m 755 berry-installer-en %{buildroot}/opt/berry
install -m 755 modules/0* %{buildroot}/opt/berry/modules
install -m 755 modules/booting/* %{buildroot}/opt/berry/modules/booting
install -m 755 modules/install/* %{buildroot}/opt/berry/modules/install
install -m 755 -d %{buildroot}/usr/share/applications/Berry
install -m 644 installer.desktop %{buildroot}/usr/share/applications/Berry

#mkdir -p %{buildroot}/etc/rc.d/init.d
#install -m 755 tools/modutils %{buildroot}/etc/rc.d/init.d/

mkdir -p %{buildroot}/usr/share/locale/ja/LC_MESSAGES
msgfmt -o %{buildroot}/usr/share/locale/ja/LC_MESSAGES/berry-installer.mo po/ja.po

## Clean Section
%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}
rm -rf $RPM_BUILD_DIR/%{name}-%{version}

## Files Section
%files
%defattr (-,root,root)
/opt/berry/*
/usr/share/applications/Berry
#/etc/rc.d/init.d/*
/usr/share/locale/ja/LC_MESSAGES

## change log
%changelog
* Thu May 14 2015 Yuichiro Nakada <berry@berry-lab.net>
- Support ext4
- To use sudo instead of gksu
* Wed Oct 31 2007 Yuichiro Nakada <berry@po.yui.mine.nu>
- Support ntfs-3g for grub.conf
- Support Japanese key for grub.conf
* Mon Jul 17 2006 Yuichiro Nakada <berry@po.yui.mine.nu>
- Bug fixed for grub and grub.conf
- Modified berry-installer-en
* Sun Feb 12 2006 Yuichiro Nakada <berry@po.yui.mine.nu>
- Modified 02-install-tools.bm for i18n
* Mon Nov 7 2005 Yuichiro Nakada <berry@po.yui.mine.nu>
- Removed berry-installer-en, installer-en.desktop
- Bug fixed for grub and lilo with udev
* Thu Aug 18 2005 Yuichiro Nakada <berry@po.yui.mine.nu>
- Modified 01-fstab.bm
* Thu Aug 4 2005 Yuichiro Nakada <berry@po.yui.mine.nu>
- Modified modutils
* Sun Jun 12 2005 Yuichiro Nakada <berry@po.yui.mine.nu>
- Added ja.po
* Wed May 18 2005 Yuichiro Nakada <berry@po.yui.mine.nu>
- Added to copy /etc/modprobe.conf, when users install Berry Linux
* Mon Feb 14 2005 Yuichiro Nakada <berry@po.yui.mine.nu>
- Added "rhgb" to grub.conf
- Bug fixed for psmouse and modutils
- Used /etc/init.d/modutils
* Fri Jan 14 2005 Yuichiro Nakada <berry@po.yui.mine.nu>
- Bug fixed for grub
* Mon Nov 22 2004 Yuichiro Nakada <berry@po.yui.mine.nu>
- Support grub
* Wed Oct 20 2004 Yuichiro Nakada <berry@po.yui.mine.nu>
- Changed for bootsplash
- Bug fix for partition
* Sat Sep 18 2004 Yuichiro Nakada <berry@po.yui.mine.nu>
- Updated berry-installer-en 0.46.5
- Version Up to 0.3-15
* Sun Sep 5 2004 Yuichiro Nakada <berry@po.yui.mine.nu>
- Updated berry-installer-en
- Version Up to 0.3-11
* Mon May 24 2004 Yuichiro Nakada <berry@po.yui.mine.nu>
- Updated berry-installer-en
- Deleted install
- Added mouse modules to rc.local for berry-installer
* Wed May 5 2004 Yuichiro Nakada <berry@po.yui.mine.nu>
- Changed berry-installer-en from http://simplylinux.punted.net/InstallingBerry.html
* Sat Apr 17 2004 Yuichiro Nakada <berry@po.yui.mine.nu>
- Changed SEARCHPATH
* Wed Apr 7 2004 Yuichiro Nakada <berry@po.yui.mine.nu>
- Added berry-installer-en from http://simplylinux.punted.net/InstallingBerry038.html
- Changed KDE Menu for KDE-3.2
* Sat Dec 13 2003 Yuichiro Nakada <berry@po.yui.mine.nu>
- Support swap
* Fri Nov 28 2003 Yuichiro Nakada <berry@po.yui.mine.nu>
- Support mbr install
* Mon Nov 24 2003 Yuichiro Nakada <berry@po.yui.mine.nu>
- Support English mode for install
* Wed Nov 19 2003 Yuichiro Nakada <berry@po.yui.mine.nu>
- Use new fs for changing device name
* Mon Sep 8 2003 Yuichiro Nakada <berry@po.yui.mine.nu>
- Added berry-installer
* Sat Jul 12 2003 Yuichiro Nakada <berry@po.yui.mine.nu>
- Create for Berry Linux
- from KNOPPIX (http://developer.linuxtag.net/knoppix/sources/)
- knoppix-hdinstall_0.39-1.tar.gz
