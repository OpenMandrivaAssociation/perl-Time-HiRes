%define upstream_name    Time-HiRes
%define upstream_version 1.9726
Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	1
Epoch:      1

Summary:    High resolution time, sleep, and alarm
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Time/Time-HiRes-%{upstream_version}.tar.gz

BuildRequires: perl-devel
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
The 'Time::HiRes' module implements a Perl interface to the 'usleep',
'nanosleep', 'ualarm', 'gettimeofday', and 'setitimer'/'getitimer' system
calls, in other words, high resolution time and timers. See the the
/EXAMPLES manpage section below and the test scripts for usage; see your
system documentation for the description of the underlying 'nanosleep' or
'usleep', 'ualarm', 'gettimeofday', and 'setitimer'/'getitimer' calls.

If your system lacks 'gettimeofday()' or an emulation of it you don't get
'gettimeofday()' or the one-argument form of 'tv_interval()'. If your
system lacks all of 'nanosleep()', 'usleep()', 'select()', and 'poll', you
don't get 'Time::HiRes::usleep()', 'Time::HiRes::nanosleep()', or
'Time::HiRes::sleep()'. If your system lacks both 'ualarm()' and
'setitimer()' you don't get 'Time::HiRes::ualarm()' or
'Time::HiRes::alarm()'.

If you try to import an unimplemented function in the 'use' statement it
will fail at compile time.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1:1.972.400-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Mon Jun 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1:1.972.400-1
+ Revision: 684828
- update to new version 1.9724

* Sun May 22 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1:1.972.200-1
+ Revision: 677401
- update to new version 1.9722

* Sat Nov 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1:1.972.100-4mdv2011.0
+ Revision: 597205
- rebuild

* Wed Jul 28 2010 Jérôme Quelin <jquelin@mandriva.org> 1:1.972.100-3mdv2011.0
+ Revision: 562438
- rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1:1.972.100-2mdv2011.0
+ Revision: 555201
- rebuild for 5.12

* Mon Mar 22 2010 Jérôme Quelin <jquelin@mandriva.org> 1:1.972.100-1mdv2010.1
+ Revision: 526426
- update to 1.9721

* Sat Feb 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1:1.972.0-1mdv2010.1
+ Revision: 505266
- update to 1.9720

* Fri Aug 07 2009 Jérôme Quelin <jquelin@mandriva.org> 1:1.971.900-1mdv2010.0
+ Revision: 411163
- rebuild using %%perl_convert_version

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 1.9719-2mdv2010.0
+ Revision: 375890
- rebuild

* Wed May 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1.9719-1mdv2010.0
+ Revision: 372651
- import perl-Time-HiRes


* Wed May 06 2009 cpan2dist 1.9719-1mdv
- initial mdv release, generated with cpan2dist



