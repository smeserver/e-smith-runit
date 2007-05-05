Summary: generic support framework for Gerrit Pape's runit package
%define name e-smith-runit
Name: %{name}
%define version 1.0.0
%define release 5
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch0: e-smith-runit-1.0.0-condrestart.patch
Patch1: e-smith-runit-1.0.0-runit17.patch
Patch2: e-smith-runit-1.0.0-runit17.patch2
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildRequires: e-smith-devtools
BuildArchitectures: noarch
Requires: runit >= 1.0.5
Provides: e-smith-daemontools = 1.7.1-09
Obsoletes: e-smith-daemontools
Obsoletes: supervise-scripts

%changelog
* Sun Apr 29 2007 Shad L. Lords <slords@mail.com>
- Clean up spec so package can be built by koji/plague

* Fri Feb 16 2007 Shad L. Lords <slords@mail.com> 1.0.0-5
- Fix signals sent to prevent errors and delays [SME: 1179]

* Fri Feb 16 2007 Shad L. Lords <slords@mail.com> 1.0.0-4
- Change runsvctrl to sv to support runit v1.7.x [SME: 1179]

* Thu Dec 07 2006 Shad L. Lords <slords@mail.com>
- Update to new release naming.  No functional changes.
- Make Packager generic

* Tue Aug 22 2006 Charlie Brady <charlie_brady@mitel.com> 1.0.0-02
- Add support for 'condrestart' param. [SME: 1870]

* Wed Mar 15 2006 Charlie Brady <charlie_brady@mitel.com> 1.0.0-01
- Roll stable stream version. [SME: 1016]

* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au> 0.0.1-06
- Bump release number only

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
