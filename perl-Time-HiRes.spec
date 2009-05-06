
%define realname   Time-HiRes
%define version    1.9719
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    High resolution time, sleep, and alarm
Source:     http://www.cpan.org/modules/by-module/Time/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel




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
%setup -q -n %{realname}-%{version} 

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


