%define upstream_name    Time-HiRes
%define upstream_version 1.9721

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Epoch:      1

Summary:    High resolution time, sleep, and alarm
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Time/%{upstream_name}-%{upstream_version}.tar.gz

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
