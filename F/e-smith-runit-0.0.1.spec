Summary: generic support framework for Gerrit Pape's runit package
%define name e-smith-runit
Name: %{name}
%define version 0.0.1
%define release 05
Version: %{version}
Release: %{release}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch0: e-smith-runit-0.0.1-03.mitel_patch
Patch1: e-smith-runit-0.0.1-04.mitel_patch
Patch2: e-smith-runit-0.0.1-05.mitel_patch
Packager: e-smith developers <bugs@e-smith.com>
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildRequires: e-smith-devtools
BuildArchitectures: noarch
Requires: runit >= 1.0.5
Provides: e-smith-daemontools = 1.7.1-09
Obsoletes: e-smith-daemontools
Obsoletes: supervise-scripts

%changelog
* Wed Jun 15 2005 Charlie Brady <charlieb@e-smith.com>
- [0.0.1-05]
- Provide more user feedback from init.d/daemontools script.
  [SF: 1218682]

* Tue Apr 26 2005 Charlie Brady <charlieb@e-smith.com>
- [0.0.1-04]
- Reopen stdin from /dev/null before running runsvdir. This prevents any
  supervised services from stealing console input from VT1's getty/console.

* Wed Dec  1 2004 Charlie Brady <charlieb@e-smith.com>
- [0.0.1-03]
- Call runsvctrl multiple times for multiple args - can't combine
  them (unlike svc).

* Tue Sep 28 2004 Charlie Brady <charlieb@e-smith.com>
- [0.0.1-02]
- Add Obsoletes header for supervise-scripts

* Fri Sep 24 2004 Charlie Brady <charlieb@e-smith.com> 0.0.1-01
- Initial - functional replacement for e-smith-daemontools 1.7.1-09.

%description
Provide integration of Gerrit Pape's runit package into a SysV init script
process environment.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
    > %{name}-%{version}-%{release}-filelist
echo "%doc COPYING" >> %{name}-%{version}-%{release}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%preun
%post
%postun

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
